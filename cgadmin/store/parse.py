# -*- coding: utf-8 -*-


def parse_db_project(new_project):
    """Parse Project from database to JSON."""
    project_data = {
        'name': new_project.name,
        'customer': new_project.customer.customer_id,
        'families': [],
    }
    for family in new_project.families:
        family_data = {
            'name': family.name,
            'panels': family.panels,
            'priority': family.priority,
            'delivery_type': family.delivery_type,
            'require_qcok': family.require_qcok,
            'samples': [],
            'existing_family': family.existing_family,
            'keep_vis': family.keep_vis,
        }
        for sample in family.samples:
            sample_data = {
                'name': sample.name,
                'sex': sample.sex,
                'status': sample.status,
                'application_tag': sample.application_tag.name if sample.application_tag else None,
                'capture_kit': sample.capture_kit,
                'source': sample.source,
                'container': sample.container,
                'container_name': sample.container_name,
                'well_position': sample.well_position,
                'quantity': sample.quantity,
                'existing_sample': sample.existing_sample,
                'exclude_analysis': sample.exclude_analysis,
            }
            for parent_id in ('father', 'mother'):
                parent_sample = getattr(sample, parent_id)
                if parent_sample:
                    sample_data[parent_id] = parent_sample.name
            family_data['samples'].append(sample_data)

            # remove None elements
            for key in list(sample_data.keys()):
                if sample_data[key] is None:
                    del sample_data[key]

        project_data['families'].append(family_data)

    return project_data
