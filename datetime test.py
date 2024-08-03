import locale
from datetime import datetime

# Set the locale to Spanish (Spain)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Get the current date
today = datetime.now()

# Format the date as a string in Spanish
date_string = today.strftime('%A, %d de %B de %Y')

print(date_string)

lyrics = """
Purple rain, purple rain, purple drank, uh (yeah, ayy)
It's a purple party, all this purple on me, uh (purple)
She gon' pop it for me (pop), pop it for me (pop)
Purple rain, purple rain, purple drank, uh (yeah)
It's a purple party, all this purple on me, uh (purple)
She gon' pop it for me (pop), pop it for me (pop)

I love you the same
And I'm sippin' purple rain
And I hope you stay the same
And I hope you stay
I love you the same
And I'm sippin' purple rain
And I hope you stay the same
And I hope you stay

Four corners on the wall, I'm goin' crazy like I'm Wemby (Yeah)
Way deep down in her water, way too deep, finna break her levee (Sweet)
I'm standin' on the wings, lemon pepper (Sweet)
Ten-seater jet, this shit forever (Sweet)
Oh, what you hot for? Give me an encore
I got the Swisher on lil' shorty on the top floor
I'm steady runnin' up a check and, no, I'm not sore
It's Hardstone to the blood, bitch, it's hardcore

[Chorus: Future & Don Toliver]
Sippin' purple, sippin' purple rain
I'm sippin' purple, sippin' purple rain
Sippin' purple, yeah, I'm sippin' purple rain
        """

split_lyrics = lyrics.splitlines()
print(len(split_lyrics))
print("\n")
print(split_lyrics)
print("\n")
while len(split_lyrics) > 14:

    print(split_lyrics[0:13])
    del split_lyrics[0:13]
    print("\n")
    print(len(split_lyrics))
print(split_lyrics)