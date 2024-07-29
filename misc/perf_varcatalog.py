import cProfile
import pstats
from metadata.dd.DdProjection import ddProj, DdProj, VarProj


def test_perf_varcatalog():
    for i in range(1000000):
        ddProj.ddElements[VarProj.intraperiod]

def test_perf_varcatalog_singleton():
    for i in range(1000000):
        DdProj().ddElements[VarProj.intraperiod]

if __name__ == "__main__":
    with cProfile.Profile() as pr:
        test_perf_varcatalog()
    
    ps = pstats.Stats(pr).sort_stats(pstats.SortKey.TIME)
    ps.print_stats()
    

    with cProfile.Profile() as pr:
        test_perf_varcatalog_singleton()
    
    ps = pstats.Stats(pr).sort_stats(pstats.SortKey.TIME)
    ps.print_stats()

    