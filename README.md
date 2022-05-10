<h1 align="center"> Blink Test 🧪</h1>



<!-- TABLE OF CONTENTS -->
<h2 id="table-of-contents"> 🐘 Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#built-with"> ➤ Built With</a></li>
    <li>
      <a href="#getting-started"> ➤ Getting Started</a>
      <ol>
      <li>
        <a href="#dependencies"> ➤ Dependencies</a>
      </li>
      <li>
        <a href="#installation"> ➤ Installation</a>
      </li>
      </ol>
    </li>
    <li>
      <a href="#usage"> ➤ Usage </a>
  </ol>
</details>


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- BUILT WITH -->
<h2 id="built-with"> 🐫 Built With</h2>

* [Python](https://www.python.org/)


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- GETTING STARTED -->
<h2 id="getting-started"> 🐤 Getting Started</h2>


<h3 id="dependencies"> Dependencies</h3>

* Python 3.9:
  ```sh
  install @https://www.python.org/downloads/
  ```


<h3 id="installation"> Installation</h3>

1. Clone the repo:
  ```sh
  git clone https://github.com/Mono2202/BlinkTest.git
  ```
2. Run ```python main.py```


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- USAGE -->
<h2 id="usage"> 🐁 Usage</h2>

<p>
 The program is a basic Forms project, which supports a certain JSON formatting file to fill out the specific forms.
 The JSON file needs to be written with this requirements:
</p>

 * "form_name" key with a form name string
 * "questions" key with the fields name and question
 * "answers" key with the fields name and available answers
 * If there is a needed field for a certain question, the field needs to be written inside an array with the key "needed_fields", and the field needs to be a key after the "needed_fields" key by itself with the correct question
 * If there is a needed field for a certain answer, the needed field needs to be a key inside to the current field, with the correct answer options inside it
 * If an answer consists of only possible answers, the possible answers need to be inside of an array
 * If an answer is an open answer, the value of the field inside the "answers" key needs to be an empty string
 * Questions need to be written with 4 more characters at the end of the string: a space, and [X] where the X is replaced with M - for mandatory question, or an O - for optional question.

<p>JSON Example: </p>

```json
{
    "form_name": "restaurant order",
    "questions":
    {
        "dish": "Choose a dish (pizza / hamburger): [M]",
        "toppings": {
            "needed_fields": ["dish"],
            "dish": {
                "hamburger": "Choose hamburger toppings: [O]",
                "pizza": "Choose pizza toppings: [O]"
            }
        },
        "cooking_level": {
            "needed_fields": ["dish"],
            "dish": {
                "hamburger": "Choose cooking level: [M]"
            }
        }
    },

    "answers":
    {
        "dish": ["pizza", "hamburger"],
        "toppings": {
            "dish": {
                "hamburger": ["pickles", "lettuce", "onions"],
                "pizza": ["olives", "tomatoes"]
            }
        },
        "cooking_level": {
            "dish": {
                "hamburger": ["M", "MW", "WD"]
            }
        }
    }
}
```

In addition to that, you can fill imported forms, just answer the given questions, and the JSON filled form will be saved in the ```filled_forms``` directory.

Imported forms will be saved @ the ```forms``` directory.
