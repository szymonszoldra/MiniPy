# MiniPy

Simple JavaScript minifier written in Python. It removes every unnecessary whitespace character, 
and minify everything to one-line file.

## How to use

Copy main.py file to directory with your JavaScript files

In terminal enter

```shell script
python main.py file_name.js
```

You can enter multiple files names

```shell script
python main.py first.js second.js third.js
```

It will make directory "minified" with all your files

## Example console output

![output](https://raw.githubusercontent.com/szymonszoldra/MiniPy/main/output.png)

## Example file
Input:

```javascript
const inputs = [...document.querySelectorAll('.controls input')];
const root = document.documentElement;

function changeStyle(e) {
  if (e.target.name === 'base') {
    return root.style.setProperty(`--${e.target.name}`, `${e.target.value}`);
  }
  root.style.setProperty(`--${e.target.name}`, `${e.target.value}px`);
}

inputs.forEach(input => input.addEventListener('input', (e) => changeStyle(e)));
```

Output:

```javascript
const inputs=[...document.querySelectorAll('.controls input')];const root=document.documentElement;function changeStyle(e){if(e.target.name==='base'){return root.style.setProperty(`--${e.target.name}`,`${e.target.value}`);}root.style.setProperty(`--${e.target.name}`,`${e.target.value}px`);}inputs.forEach(input=>input.addEventListener('input',(e)=>changeStyle(e)));
```
