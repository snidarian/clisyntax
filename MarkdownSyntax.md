<!-- remember in vs code to use ctrl + shift +v to pull up .md preview window -->

# This is a Markdown syntax language reference file.



## Headers

##### Note that using the largest header creates a section divider beneath it.

* This is a bullet point
* This is a second bullet point
* This is a third bullet point etc...
* Mark sure there's a space after the asterisk

## Control header font size with how many '#' number signs you use.
### Size three header
#### Size four header
##### Size five header

---

## LINE DIVIDERS
 Create a line divider with a triplet of the following characters:
* Three asterisks
* Three underscores
* Three dashes

> ##### Note that all three of these methods create the same line divider


***


## QUOTES

> This is a quote and as you see it is given a spotlight so to speak

> To make a quote, you use the '>' right angle bracket like so

___

## EMPHASIS


### Creating Bold Text
> Add emphasis with two asterisks '**' to open bold text and two more to close it.

**bold text**

>  bold italic text by putting two underscores before and after text

__Bold with italics__

### Creating Italic Text
> Create italic text with one asterisk or underscore to open and close

*This is italics*

_This is also italics_


## Using Bold and italics simoultaneously in the same sentence

>There once was a cold old haggard woman who wished with all her heart that she could have found love while she was still young. There was once a nice and sturdy young man who had asked her _"My sweet, Melinda, will you marry me?"_ But she had emphatically replied **NO!** hoping that someone better would come along. But now in the solemn gloom of her dilapitated study it was her remorse that looked with distate on her so hasty refusal with __tacit dissaproval__ of her youthful indicretion.

---

## LISTS

You can create lists with asterisks, dashes, plus signs,
* list item using *
+ list item using +
- list item using -

> ##### Note that again these all make the same list item bullet points.

### Sublists

* Create Sublists
    * lists simply by
      * adding \t (tabs)
        * before additonal
          * sublist items
            * And this can continue
              * as long as you like


### Ordered lists

1. Simply write the number
2. and a period and then
3. you're good to go!




---

## LINKS

Create links by surrounding the link with angle brackets

<http://www.urmom.com>


### Create a link with custom text with [custom text] followed by (weblink)

[Custom link text](http://www.urmom.com)


> ##### Note that there's no space between the square brackets and the parenthesis
---

## VARIABLES

> Create variables by creating a key in square brackets and then a colon followed by the variables content.

[var1]: http://www.urmom.com

#### Below I reference the variable with using square brackets

[Link to website][var1]

> Note that when referencing the content of a variable you must use square brackets.

---

## Quick links to Headers

When you create a header a header ID is create which can move you back to that header.

Now This header ID is the same as the content of the header **EXCEPT** that:
- upper case characters are replaced by lower case characters
- spaces (blanks) are replaced by dashes (-)

so below would be a link to the 'lists' section Headers
[link to Lists header](#lists)

> When you click on the above list it will take you to the LISTS header.

---

## IMAGES

Images are the same as links except that:
- an exclamation mark is used before custom text reference to an image

[image custom text]: (https://4.bp.blogspot.com/_w6WuukLvqx8/TK9y9pM9RVI/AAAAAAAAA1w/gkCszGgtBTY/s1600/jellyfish1a.jpg)

![image link][image custom text]

---

## Referencing code blocks and highlighting code

```
use three backticks above and below to open and close a block of text

```

```enclosing text with three backticks will highlight the code```


> ```You can combine this with an angle bracket to produce quoted & highlighted code```


---

## TABLES

- Create table headers, columns, and rows by separating text with pipes
- separate columns from the first row with pipes and dashes
    - Note it doesn't matter  if everything lines up perfectly just make the number of pipes is correct



| Header 1 | Header 2 | header 3 | header 4 | header 5 |
|  --- | --- | --- | --- | --- |
| Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
| Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
| Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
| Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |

> Repeat the above columns separated by pipes for each additional row you wish to create.

## Aligning text within a table
By inserting colons (:) on either ends of the dashes (or on both sides of the dash divider) that form the divider between the first row and the header row you can align text in each of the corresponding columns

> For example.

| Aligned Left | Centered | Aligned Right |
| :----------- | :------: | ------------: |
| text | text | text |

---

<h1>Markdown and HTML</h1>

```
<h1>Markdown and HTML</h1> or # Markdown and HTML
```
So since markdown gets converted to HTML anyway you can also write HTML.
Most of the stuff you can do with HTML you can also do with markdown.
> For instance the above header is written in HTML but could just as easily be written with a # pound sign as if we wanted to write a header with the markdown language.



# Markdown and CSS

The same applies to writing CSS and markdown:
For instance if you wanted to write a ```<style></style>``` tag.
<style>
    p {
        color: teal
    }
</style>

```
<style>
    p {
        color: teal
    }
</style>
```



> **Notice that the above ```<style>``` tag uses CSS to turn nearly all non-header and non-list-item or non table-text to the color teal.**









