from metadata.dd.DdProjection import VarProj
from metadata.dd.DdS2 import VarS2



class DfMdProj:
    def __init__(self) :
        self.mdPksTrajectoire = [VarProj.cdTrajectoire, VarProj.dtTrajectoire]
        self.mdPksScPer = [VarProj.scenario, VarProj.period]
        self.mdPksScPerIntra = [*self.mdPksScPer, VarProj.intraperiod]
        self.mdPksScPerEv = [*self.mdPksScPer, VarProj.evenement]

dfMdProj = DfMdProj()