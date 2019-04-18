import argparse
from .beautify import plot


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--logdir', default='./logdir',
                        type=str, help='logdir to event file')
    parser.add_argument('--smooth', default=100, type=float,
                        help='window size for average smoothing')
    parser.add_argument('--color', default='#4169E1',
                        type=str, help='HTML code for the figure')

    args = parser.parse_args()
    params = vars(args)  # convert to ordinary dict

    plot(params, show=True)


if __name__ == '__main__':
    main()
