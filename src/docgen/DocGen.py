import re

from metadata.dd.DdActif import ddActif
from metadata.dd.DdAlm import ddAlm
from metadata.dd.DdCommun import ddCommun
from metadata.dd.DdFgx import ddFgx
from metadata.dd.DdGse import ddGse
from metadata.dd.DdPassifEp import ddPassifEp
from metadata.dd.DdProjection import ddProj
from metadata.dd.DdS2 import ddS2
from metadata.dd.DdStratInv import ddStratInv
from metadata.dfmd.DfMdActif import dfMdActif
from metadata.dfmd.DfMdPassifEp import dfMdPassifEp
from metadata.dfmd.DfMdGse import dfMdGse
from metadata.dfmd.DfMdS2 import dfMdS2
from utils.VarCatalogGbl import VarCatalogGbl
from utils.VarCatalog import VarCatalog
from utils.DfMd import DfMd

def ddToDf(dd : VarCatalog) -> list[list]:
    ddList = [[k,f'{v.description}\nType : {v.type}\nValeurs possibles : {v.valeursPossibles}'] for k,v in dd.ddElements.items()]
    return ddList

def getRstContentDdAsTable(dd : VarCatalog) -> str:
    
    outputLines = []

    outputLines.extend([f'.. raw:: html', ''])
    for k,v in dd.ddElements.items():
        outputLines.extend([f'   <a id="{k.__str__()}"></a>', ''])
        

    outputLines.extend([
        '.. list-table::',
        '   :widths: 20 10 30',
        '   :header-rows: 1',
        '   :class: table-custom',
        '',
        '   * - Variable',
        '     - Type',
        '     - Description',
    ])

    for k,v in dd.ddElements.items():

        outputLines.extend(
            [
                f'   * -  {k.__str__()}',
                '     - ' + f'{v.data_type}',
                '     - ' + f'{v.description}',
            ]
        )
        
        outputLines.append('')

    return '\n'.join(outputLines)

def getRstContentDdAsGlossary(dd : VarCatalog) -> str:
    
    outputLines = [
        '.. glossary::',
        '\t:sorted:',
        ''
    ]

    for k,v in dd.ddElements.items():

        outputLines.extend(
            [
                '\t' + k.__str__(),
                '',
                '\t\t' + f'**Description :** {v.description}',
                '',
                '\t\t' + f'**Type :** {v.data_type}',
                '',
            ]
        )
        
        outputLines.append('')

    return '\n'.join(outputLines)


def getRstContentDictionnaireDonnees() -> str:

    return '\n'.join(
        [
            'Catalogue des données',
            '=====================',
            '',
            'Projection',
            '----------',
            '',
            getRstContentDdAsTable(ddProj),
            '',
            'Données communes',
            '----------------',
            '',
            getRstContentDdAsTable(ddCommun),
            '',
            'Variables économiques (GSE)',
            '---------------------------',
            '',
            getRstContentDdAsTable(ddGse),
            '',
            'Actif',
            '-----',
            '',
            getRstContentDdAsTable(ddActif),
            '',
            'Passif',
            '------',
            '',
            getRstContentDdAsTable(ddPassifEp),
            '',
            'Frais généraux',
            '--------------',
            '',
            getRstContentDdAsTable(ddFgx),
            '',
            'ALM',
            '---',
            '',
            getRstContentDdAsTable(ddAlm),
            '',
            "Stratégie d'investissement",
            '--------------------------',
            '',
            getRstContentDdAsTable(ddStratInv),
            '',
            "Solvabilité 2",
            '-------------',
            '',
            getRstContentDdAsTable(ddS2),
            '',
        ]
    )

def getDfHref(el : str) -> str:
    return ':df:`' + el + '`'

def getRstContentDfMdRegistryAsTable(dfMdCatalog, dd : VarCatalog) -> str:
    outputLines = []
    for attr, value in vars(dfMdCatalog).items():
        if isinstance(value, DfMd):
            dfMd : DfMd = value

            outputLines.extend(['.. raw:: html',''])
            outputLines.extend([f'   <a id="{re.sub(r'^md', '', attr.__str__())}"></a>',''])
            
            outputLines.extend([f'{re.sub(r'^md', '', attr.__str__())}'])
            outputLines.extend([''.join('^' for _ in range(len(re.sub(r'^md', '', attr.__str__())))),''])
            outputLines.extend([
                f'.. list-table::',
                '   :widths: 3 25 10 40',
                '   :header-rows: 1',
                '   :class: table-custom',
                '',
                '   * - Pk',
                '     - Variable',
                '     - Type',
                '     - Description',
            ])

            for var in dfMd.pks:
                outputLines.extend(
                    [
                        '   * - :octicon:`key`',
                        '     - ' + var.__str__(),
                        '     - ' + f'{dd.ddElements[var].data_type}',
                        '     - ' + f'{dd.ddElements[var].description}',
                    ]
                )

            for var in dfMd.columns:
                outputLines.extend(
                    [
                        '   * - ',
                        '     - ' + var.__str__(),
                        '     - ' + f'{dd.ddElements[var].data_type}',
                        '     - ' + f'{dd.ddElements[var].description}',
                    ]
                )
    
    outputLines.extend(['',''])

    return '\n'.join(outputLines)

def getRstContentDfMdRegistryAsGlossaryOld(dfMdRegistry) -> str:
    
    outputLines = [
        '.. glossary::',
        '\t:sorted:',
        ''
    ]

    for attr, value in vars(dfMdRegistry).items():
        if isinstance(value, DfMd):
            dfMd : DfMd = value
            outputLines.extend(
                [
                    '\t' + re.sub(r'^md', '', attr.__str__()),
                    '',
                    '\t\t' + f'**Clés primaires :** {[getDfHref(el.__str__()).__str__() for el in dfMd.pks]}\n',
                    '',
                    '\t\t' + f'**Colonnes :** {[getDfHref(el.__str__()).__str__() for el in dfMd.columns]}\n',
                    '',
                ]
            )

    return '\n'.join(outputLines)

def getRstContentDfMdRegistry() -> str:

    return '\n'.join(
        [
            'Format des dataframes',
            '=====================',
            '',
            'Variables économiques (GSE)',
            '---------------------------',
            '',
            getRstContentDfMdRegistryAsTable(dfMdGse, VarCatalogGbl()),
            '',
            'Actif',
            '-----',
            '',
            getRstContentDfMdRegistryAsTable(dfMdActif, VarCatalogGbl()),
            '',
            'Passif',
            '------',
            '',
            getRstContentDfMdRegistryAsTable(dfMdPassifEp, VarCatalogGbl()),
            '',
            'Alm',
            '---',
            '',
            # getRstContentDfMdRegistryAsTable(dfMdAlmCr, VarCatalogGbl()),
            '',
            'Solvablité 2',
            '------------',
            '',
            getRstContentDfMdRegistryAsTable(dfMdS2, VarCatalogGbl()),
            '',
            
        ]
    )



