import random
import sys

def main(infilename, outfilename, percentaje):  # percentaje float in (0,1) 
    with open(infilename) as i_f:
        with open(outfilename, 'w') as o_f:
            for line in i_f:
                if random.random()<=percentaje:
                    o_f.write(line)


if __name__=="__main__":
    if len(sys.argv)<4:
        print(f"No hay un número adecuado de parámetros: {sys.argv[0]} <infilename> <outfilename> <percentaje")
        exit(1)
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    percentaje = float(sys.argv[3])
    main(infilename, outfilename, percentaje)
