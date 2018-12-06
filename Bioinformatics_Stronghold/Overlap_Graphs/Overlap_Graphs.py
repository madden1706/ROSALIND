from Bio import SeqIO


# x = [edge1, edge2] #  adjacency list = list of unique edges connecting a node.

def overlap_graph(input, overlap):
    """Takes arguments of an input fasta file and an overlap length of the suffix/prefix.
    Returns seq IDs in a file as X(suffix) (prefix)Y"""

    sequence_dict = {}
    seq_id_list = []

    for seq_record in SeqIO.parse(input, "fasta"): # change input variable.
        sequence_dict[seq_record.id] = seq_record.seq
        seq_id_list.append(seq_record.id)

    adjacency_list= []

    index = overlap

    for id in seq_id_list:
        neg_index = (index * -1)
        for k in sequence_dict:

            if id == k:
                pass

            elif id != k:
                if sequence_dict[id][neg_index:] == sequence_dict[k][0:index]:
                    adjacency_list.append(f"{id} {k}".format(id=id, k=k))

                    #print("\nyes")
                    #print(id, sequence_dict[id][neg_index:], "and", k, sequence_dict[k][0:index], "\n")
                else:
                    pass

                    #print("no")
                    #print(id, sequence_dict[id][neg_index:], "and", k, sequence_dict[k][0:index])
    open("output.txt", "w")
    with open("output.txt", "a") as out:
        for x in adjacency_list:
            out.write(f"{x}\n".format(x=x))

overlap_graph("input.fasta", 3)

