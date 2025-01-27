from exercises import *


def validate_answer(output, reference):
    """a fairly forgiving test ;)"""
    if output == reference:
        return True
    elif str(reference) in str(output):
        return True

    return False


def test_suite():
    # exercise 1
    e1_values = [
        (100, 0.10, 110),
        (50, 0.20, 60),
        (75, 0.30, 97.5),
        (3441321.5, 0.10, 3785453.65),
        (1669.00, 0.19, 1986.11),
    ]
    print("Running tests for exercise 1...")
    for price, tax_rate, reference in e1_values:
        assert validate_answer(
            price_with_taxes(price, tax_rate), reference
        ), f"Failed for {price} with rate {tax_rate}"
        print(f"Passed for {price} with rate {tax_rate} = {reference}")
    print()

    # exercise 2
    e2_values = [
        ("Frodo", "Baggins", 13),
        ("Samwise", "Gamgee", 14),
        ("Gandalf", "the Grey", 16),
        ("Aragorn", "son of Arathorn", 23),
        ("Legolas", "Greenleaf", 17),
        ("Gimli", "son of Glóin", 18),
        ("Boromir", "of Gondor", 17),
        ("Galadriel", "of Lothlórien", 23),
        ("Meriadoc", "Brandybuck", 19),
        ("Peregrin", "Took", 13),
        ("Elrond", "Half-elven", 17),
        ("Arwen", "Undómiel", 14),
        ("Saruman", "the White", 17),
    ]

    print("Running tests for exercise 2...")
    for l, r, reference_length in e2_values:
        assert validate_answer(
            length_of_name(l, r), reference_length
        ), f"Failed for {' '.join([l, r])}"
        print(f"Passed for {' '.join([l, r])} = {reference_length}")
    print()

    # exercise 3
    e3_values = [
        (1, 104342.2862388421),
        (482.95, 50392107.1390488),
        (553.66, 57770150.198997326),
        (96.22, 10039814.781901387),
        (853.25, 89030055.73329203),
        (550.63, 57453993.07169363),
    ]
    print("Running tests for exercise 3...")
    for price, reference in e3_values:
        assert validate_answer(
            bitcoin_price_in_euros(price), reference
        ), f"Failed for {price}"
        print(f"Passed for {price} = {reference}")
    print()

    e4_values = [
        (
            "Once upon a time in the enchanted hills of Glitterdale, a young unicorn named Sparkle decided she wanted to learn how to snowboard. One frosty morning, she trotted down to the snowy slopes, her iridescent mane shimmering in the sunlight. With a magical snowboard crafted from moonlight and fairy dust, Sparkle strapped in her hooves. At first, she wobbled and tumbled, causing a flurry of snow to erupt around her. The woodland creatures gathered to cheer her on as she persevered. After a few practice runs, Sparkle discovered the secret to snowboarding: believing in herself. With a burst of confidence, she glided down the slope, performing flips and spins, leaving a trail of sparkling snowflakes behind her. From that day on, Sparkle became the first unicorn snowboard champion, inspiring all the creatures of Glitterdale to embrace their dreams, no matter how fantastical.",
            "a",
        ),
        (
            "In a land made entirely of sweets, a brave hero named Marshy, the Marshmallow, lived with a mission. One day, the Candy Kingdom faced a dire threat from the evil Lord Licorice, who aimed to cover it in darkness. Marshy, with his soft and squishy exterior, donned a cape made of gummy bear fabric and set off on an adventure to save his home. Armed with a trusty chocolate sword, he journeyed through the Gumdrop Forest, where he met allies like Captain Caramel and Princess Peppermint. Together, they faced challenges like the Sour Patch Swamp and the Chocolate River, overcoming obstacles with teamwork and courage. Finally, they reached Lord Licorice's lair, where a fierce battle ensued. With a clever strategy, Marshy used his fluffiness to bounce around and dodge attacks, ultimately defeating Lord Licorice by trapping him in a sticky taffy net. The Candy Kingdom was saved, and Marshy became a legend, celebrated for his bravery and determination. From that day on, the kingdom remained a sweet place, and Marshy continued to protect it, always ready for the next adventure.",
            "d",
        ),
    ]

    print("Running tests for exercise 4...")
    for story, reference in e4_values:
        r4 = last_character_third_word(story)
        assert validate_answer(r4, reference), f"Failed for {story}"
        print(f"Passed for '{story[:50]} ...' = {reference}")
    print()

    e5_values = [
        ([1, 100, 2032130, 300051, 4342140000], 868894456.4),
        ([1, 100, 2000, 30000, 400000], 86420.2),
        ([5, 50, 500, 5000, 50000], 11111.0),
        ([0.1, 0.5, 1.1, 2.5, 3.3], 1.5),
        ([-10, -5, 0, 5, 10], 0.0),
        ([7.2, 14.6, 21.9, 29.3, 35.7], 21.740000000000002),
    ]
    print("Running tests for exercise 5...")
    for l, r in e5_values:
        assert validate_answer(compute_average(l), r), f"Failed on {l}"
        print(f"Passed on {l} = {r}")


if __name__ == "__main__":
    test_suite()
