#!/usr/bin/python

#                        _
#  _ __ ___   __ _  __ _(_) ___   _ __  _   _
# | '_ ` _ \ / _` |/ _` | |/ __| | '_ \| | | |
# | | | | | | (_| | (_| | | (__ _| |_) | |_| |
# |_| |_| |_|\__,_|\__, |_|\___(_) .__/ \__, |
#                  |___/         |_|    |___/
# v1.0.0
#                        <Directed ByABGEO />

import random


def get_random_answer():
    """Get random answer.

    Returns:
        Random answer from answers array.
    """

    # Generate random number
    rand = random.randint(0, 7)

    answers = [
        "უეჭველი.",
        "ამ ცხოვრებაში არა.",
        "შენ ამას შეძლებ.",
        "სხვა დროს მკითხე.",
        "კონცენტრირდი და ხელახლა მკითხე.",
        "რატომ მაბრაზებ?! სხვა რამე მკითხე.",
        "ჩემი პასუხია - არა.",
        "რატომაც არა.",
    ]

    # Return random answer from array
    return answers[rand]
# End get_random_answer()


def main():
    question = input('მკითხე რამე ან დააჭირე Enter-ს გამოსასვლელად: ')

    while question != '':
        print('\t- ' + get_random_answer())

        question = input('\nკიდევ მკითხე რამე ან დააჭირე Enter-ს გამოსასვლელად: ')
    # End while

    print('\n\nმომავალ შეხვედრამდე! გელოდები ახალი კითხვებით.')
# End main()


if __name__ == "__main__":
    main()
