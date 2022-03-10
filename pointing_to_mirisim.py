import argparse

from miricoord.apt2dither.apt2dither import make_dith_file

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("ifile", help="pointing file from APT")
    args = parser.parse_args()

    ofile = args.ifile.replace(".pointing", ".dat")
    make_dith_file(f"apt_pointings/{args.ifile}",
                   f"mirisim_dithers/{ofile}")
