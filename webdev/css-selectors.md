# Useful CSS selectors

* http://blog.teamtreehouse.com/5-useful-css-selectors
* http://www.w3.org/TR/css3-selectors/#selectors

CSS selectors provide a way to target elements based on their positions relative to other elements.

## `:first-child` and `:last-child`

`:first-child` only selects the element that is the first child element of its parent element.

```css
li:first-child {
  border-top: none;
  font-weight: bold;
}
```

Similarly for `:last-child`.

```css
li:last-child {
  border-bottom: none;
}
```

## `:nth-child`

`:nth-child` lets us choose elements based on their ordering within a parent element. It requires an argument to denote the selection criteria.

We can pass in an integer. The example below will only select `li` elements that are the third child of their parents.

```css
li:nth-child(3) {
  background-color: tomato;  
}
```

We can pass in the keywords `odd` and `even`, as below.

```css
li:nth-child(even) {
  color: white;
  background-color: black;
}
```

We can use the `n` keyword to construct expressions to select children.

This selector will select the third, fifth, seventh, etc, `li` children elements.

```css
li:nth-child(2n+3) {}
```

This selector will select all children `li` elements up to and including the fifth child.

```css
li:nth-child(-n+5) {}
```

Although, for complex selection rules, you should consider just using a class instead.

## `:nth-of-type`

`:nth-of-type` selects an element based on its position within a parent's list of children of the same type specified.

This selector will only select the fourth image on the page.

```css
img:nth-of-type(4) {}
```

## `:target` pseudo-class

The `:target` pseudo-class selects the element that has the same identifier as the fragment identifier of the current URI.

For example, if the page has these two elements:

```html
<div id="introduction">My Essay</div>
<div id="conclusion">The end.</div>
```

The CSS rule:

```css
:target {
  border: 5px solid blue;
}
```

Will select the element with the identifier `introduction` if the browser navigates to `page#introduction`, and likewise for the `conclusion` identifier.

## `::before` and `::after` pseudo-elements

`::before` will insert content before the contents of the selected element. The content is specified with the `content` property, which must be assigned some value (or just `''`).

This rule would put an icon to the right of an element with the `pdf` class.

```css
.pdf::before {
  content: url(img/pdf.png);
  margin-right: 10px;
}
```

This rule will insert quotation marks at either end of the contents of `blockquote` elements.

```css
blockquote::before {
  content: "\275D";   /* unicode icon for opening mark */
  margin-right: 20px;
}

blockquote::after {
  content: "\275E";   /* unicode icon for closing mark */
  margin-left: 20px;
}
```
