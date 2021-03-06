# -*- coding: utf-8 -*-
import itertools

SOURCES = ['blood', 'saliva', 'tissue (fresh frozen)', 'tissue (FFPE)',
           'cell line', 'nail', 'other']
SEXES = ['male', 'female', 'unknown']
STATUSES = ['affected', 'unaffected', 'unknown']
CONTAINERS = ['96 well plate', 'Tube']
DELIVERY_TYPES = ['fastq', 'scout', 'custom']
APPLICATION_CATEGORIES = ['Whole genome', 'Whole exome', 'Panel', 'RNA',
                          'Microbial']
APPLICATIONS = {
    'Whole genome': ['WGSPCFC030', 'WGSPCFC060', 'WGSPCFC090', 'WGTPCFC030',
                     'WGLPCFC030', 'WGSLIFC030', 'WGSLIFC060', 'WGSLIFC090',
                     'WGTLIFC030'],
    'Whole exome': ['EXOSXTR100', 'EXOSXTR075', 'EXOSXTR060', 'EXOSXTR030',
                    'EXTSXTR100', 'EXTSXTR075', 'EXTSXTR060',
                    'EXTSXTR045', 'EXTSXTR030', 'EXOSLIR100', 'EXOSLIR075',
                    'EXOSLIR060', 'EXOSLIR030', 'EXTSLIR100', 'EXTSLIR075',
                    'EXTSLIR060', 'EXTSLIR030', 'EXOSFFR100', 'EXOSFFR075'],
    'Panels': ['EFTSXTR020', 'EFTSXTR030', 'EFTSLIR020', 'EFTSLIR030',
               'MHPSXTR025', 'MHPSLIR025', 'CCPSLIR005'],
    'RNA': ['RNADEPR030', 'RNLDEPR030', 'RNAPOAR030', 'RNLPOAR030']
}
ALL_APPLICATIONS = list(itertools.chain.from_iterable(APPLICATIONS.values()))
PANELS = ['mtDNA', 'IBMFS', 'PIDCAD', 'SKD', 'OMIM-AUTO', 'ID', 'CTD', 'NJU', 'ATX',
          'SPG', 'Ataxi', 'AD', 'MIT', 'ENDO', 'IEM', 'EP', 'HYP', 'DSD', 'SEXDIF',
          'SEXDET', 'NMD', 'PID', 'ET', 'PEDHEP']
PRIORITIES = ['standard', 'priority', 'express', 'research']
CUSTOMERS = [('cust003', 'CMMS'), ('cust002', 'Klinisk Genetik')]
WELL_POSITIONS = ['A:1', 'B:1', 'C:1', 'D:1', 'E:1', 'F:1', 'G:1', 'H:1',
                  'A:2', 'B:2', 'C:2', 'D:2', 'E:2', 'F:2', 'G:2', 'H:2',
                  'A:3', 'B:3', 'C:3', 'D:3', 'E:3', 'F:3', 'G:3', 'H:3',
                  'A:4', 'B:4', 'C:4', 'D:4', 'E:4', 'F:4', 'G:4', 'H:4',
                  'A:5', 'B:5', 'C:5', 'D:5', 'E:5', 'F:5', 'G:5', 'H:5',
                  'A:6', 'B:6', 'C:6', 'D:6', 'E:6', 'F:6', 'G:6', 'H:6',
                  'A:7', 'B:7', 'C:7', 'D:7', 'E:7', 'F:7', 'G:7', 'H:7',
                  'A:8', 'B:8', 'C:8', 'D:8', 'E:8', 'F:8', 'G:8', 'H:8',
                  'A:9', 'B:9', 'C:9', 'D:9', 'E:9', 'F:9', 'G:9', 'H:9',
                  'A:10', 'B:10', 'C:10', 'D:10', 'E:10', 'F:10', 'G:10',
                  'H:10', 'A:11', 'B:11', 'C:11', 'D:11', 'E:11', 'F:11',
                  'G:11', 'H:11', 'A:12', 'B:12', 'C:12', 'D:12', 'E:12',
                  'F:12', 'G:12', 'H:12']
CAPTURE_KITS = ['Agilent Sureselect CRE', 'Agilent Sureselect V5',
                'SureSelect Focused Exome', 'other']
