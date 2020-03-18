# Your task is to run Prim's minimum spanning tree algorithm on this graph.
# You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative
# IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation
# of Prim's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge,
# try implementing a heap-based version. The simpler approach, which should already give you a healthy speed-up,
# is to maintain relevant edges in a heap (with keys = edge costs).
# The superior approach stores the unprocessed vertices in the heap.
# Note this requires a heap that supports deletions, and you'll probably need to maintain some
# kind of mapping between vertices and their positions in the heap.
