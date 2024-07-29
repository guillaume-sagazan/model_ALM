import cProfile
import pstats
from metadata.dd.DdProjection import VarProj


def test_perf_str():
    for i in range(1000000):
        str = "intraperiod"

def test_perf_varcatalog():
    for i in range(1000000):
        str = VarProj.intraperiod

if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    test_perf_str()
    test_perf_varcatalog()
    pr.disable()
    ps = pstats.Stats(pr).sort_stats('cumulative')
    ps.print_stats()