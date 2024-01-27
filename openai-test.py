import os

from dotenv import load_dotenv
from openai import OpenAI

# Load OpenAI API key from environment variables
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=openai_api_key)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
         "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative "
                    "flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

'''ChatCompletionMessage( content="In the realm of code where lines align,\nLies a construct truly divine,
\nA dance of calling from within,\nA concept known as recursion.\n\nLike a reflection in a mirror's glare,
\nA function calls itself with care,\nDescending down a recursive spell,\nInto the depths where wonders 
dwell.\n\nJust like a matryoshka, nested and neat,\nLayers of repetition it will repeat,\nA problem divided, 
smaller and small,\nUntil a base case breaks the fall.\n\nWith elegance, it loops and loops,\nLike an echo bouncing 
through the hoops,\nDeeper and deeper, it explores,\nUnwinding the mysteries it adores.\n\nWith graceful bounds, 
it conquers heights,\nSolving puzzles, unlocking insights,\nAs it spirals through each recursive ring,\nBeauty in its 
mathematical wings.\n\nBut beware, dear coder, of the infinite snare,\nA loop without an end, a dreadful affair,
\nWith recursion, caution must abound,\nBase cases found, they must be sound.\n\nSo embrace recursion, 
dear programmer's peers,\nA tool that's been cherished for countless years,\nIn this dance of code, it thrives and 
thrills,\nUnlocking wonders, climbing digital hills.", role='assistant', function_call=None, tool_calls=None )'''
print(completion.choices[0].message.content)
