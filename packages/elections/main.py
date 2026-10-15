from packages.elections.src.elections import processed_data, views


def main():
    """Main function to run the election data processing and views."""

    data = processed_data.run()
    views.run(data)

    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
