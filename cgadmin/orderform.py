# -*- coding: utf-8 -*-
import xlrd
from cgadmin.lims import SEX_MAP

REV_SEX_MAP = {value: key for key, value in SEX_MAP.items()}


def parse_orderform(excel_path):
    """Parse out information from an order form."""
    workbook = xlrd.open_workbook(excel_path)
    orderform_sheet = workbook.sheet_by_name('orderform')
    raw_samples = relevant_rows(orderform_sheet)
    parsed_samples = [parse_sample(raw_sample) for raw_sample in raw_samples]
    parsed_families = group_families(parsed_samples)
    families = [expand_family(family_id, parsed_family) for
                family_id, parsed_family in parsed_families.items()]

    customers = set(family['customer'] for family in families)
    if len(customers) != 1:
        raise ValueError("invalid customer information: {}".format(customers))

    new_project = {
        'customer': customers.pop(),
        'families': families,
    }
    return new_project


def expand_family(family_id, parsed_family):
    """Fill-in information about families."""
    new_family = {'name': family_id, 'samples': []}
    samples = parsed_family['samples']
    delivery_types = set(raw_sample['delivery_type'] for raw_sample in samples)
    if len(delivery_types) != 1:
        raise ValueError("incorrect delivery types: {}".format(delivery_types))
    new_family['delivery_type'] = delivery_types.pop()

    require_qcoks = set(raw_sample['require_qcok'] for raw_sample in samples)
    if True in require_qcoks:
        new_family['require_qcok'] = True

    priorities = set(raw_sample['priority'] for raw_sample in samples)
    if len(priorities) > 1 and 'priority' in priorities:
        new_family['priority'] = 'priority'
    else:
        new_family['priority'] = priorities.pop()

    customers = set(raw_sample['customer'] for raw_sample in samples)
    if len(customers) != 1:
        raise ValueError("invalid customer information: {}".format(customers))
    new_family['customer'] = customers.pop()

    gene_panels = set()
    for raw_sample in samples:
        if raw_sample['panels']:
            gene_panels.update(raw_sample['panels'])
        new_sample = {
            'name': raw_sample['name'],
            'container': raw_sample['container'],
            'container_name': raw_sample['container_name'],
            'sex': raw_sample['sex'],
            'application_tag': raw_sample['application_tag'],
            'source': raw_sample['source'],
        }
        for key in ('container', 'container_name', 'well_position', 'quantity',
                    'status'):
            if raw_sample[key]:
                new_sample[key] = raw_sample[key]

        for parent_id in ('mother', 'father'):
            if raw_sample[parent_id]:
                new_sample[parent_id] = raw_sample[parent_id]
        new_family['samples'].append(new_sample)
    if len(gene_panels) > 0:
        new_family['panels'] = list(gene_panels)

    return new_family


def group_families(parsed_samples):
    """Group samples on family."""
    raw_families = {}
    for sample in parsed_samples:
        family_id = sample['family']
        if family_id not in raw_families:
            raw_families[family_id] = {
                'samples': [],
            }
        raw_families[family_id]['samples'].append(sample)
    return raw_families


def parse_sample(raw_sample):
    """Parse a raw sample row from order form sheet."""
    if ':' in raw_sample['UDF/Gene List']:
        raw_sample['UDF/Gene List'] = raw_sample['UDF/Gene List'].replace(':', ';')

    if raw_sample['UDF/priority'].lower() == 'förtur':
        raw_sample['UDF/priority'] = 'priority'

    sample = {
        'name': raw_sample['Sample/Name'],
        'container': raw_sample.get('Container/Type'),
        'container_name': raw_sample.get('Container/Name'),
        'well_position': raw_sample.get('Sample/Well Location'),
        'delivery_type': raw_sample.get('UDF/Data Analysis'),
        'sex': REV_SEX_MAP[raw_sample['UDF/Gender'].strip()],
        'panels': (raw_sample['UDF/Gene List'].split(';') if
                   raw_sample.get('UDF/Gene List') else None),
        'require_qcok': True if raw_sample['UDF/Process only if QC OK'] else False,
        'quantity': raw_sample['UDF/Quantity'] if raw_sample.get('UDF/Quantity') else None,
        'application_tag': raw_sample['UDF/Sequencing Analysis'],
        'source': raw_sample['UDF/Source'].lower(),
        'status': raw_sample['UDF/Status'].lower(),
        'customer': raw_sample['UDF/customer'],
        'family': raw_sample['UDF/familyID'],
        'mother': raw_sample['UDF/motherID'] if raw_sample['UDF/motherID'] else None,
        'father': raw_sample['UDF/fatherID'] if raw_sample['UDF/fatherID'] else None,
        'priority': raw_sample['UDF/priority'].lower(),
        'capture_kit': (raw_sample['UDF/Capture Library version'] if
                        raw_sample['UDF/Capture Library version'] else None),
        'comment': raw_sample['UDF/Comment'] if raw_sample['UDF/Comment'] else None,
    }
    return sample


def relevant_rows(orderform_sheet):
    """Get the relevant rows from an order form sheet."""
    raw_samples = []
    current_row = None
    for row in orderform_sheet.get_rows():
        if row[0].value == '</SAMPLE ENTRIES>':
            break

        if current_row == 'header':
            header_row = [cell.value for cell in row]
            current_row = None
        elif current_row == 'samples':
            values = [str(cell.value) for cell in row]
            if values[0]:
                # skip empty rows
                sample_dict = dict(zip(header_row, values))
                raw_samples.append(sample_dict)

        if row[0].value == '<TABLE HEADER>':
            current_row = 'header'
        elif row[0].value == '<SAMPLE ENTRIES>':
            current_row = 'samples'
    return raw_samples
