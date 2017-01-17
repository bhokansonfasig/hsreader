from __future__ import print_function
import hsreader as hs
import cPickle as pickle

datadir = "/data/exp/IceCube/2014/internal-system/hit-spooling/0815"

def time_filter(hit):
    t0 = 195495400000000000
    t_max = 195495600000000000
    if hit.utc<t0:
        return False
    if hit.utc>t_max:
        raise StopIteration
        # return False
    return True


# all_hits = hs.load_stream(datadir,time_filter)

hs.write_h5(datadir,"test_output",time_filter)

# print(len(all_hits))
# print(all_hits[0])
# print(all_hits[-1])

# last_hit = all_hits[0]
# for hit in all_hits[1:]:
#     if hit.utc<last_hit.utc:
#         print("ERROR: ",hit.utc,"<",last_hit.utc)
#     if hit.utc==last_hit.utc:
#         print("WARNING: ",hit.utc,"=",last_hit.utc)
#     last_hit = hit

# i = 0
# for hit in all_hits:
#     if i%10000000==0:
#         print(i,hit)
#     i += 1
#
# print("Grabbed",i,"hits")
