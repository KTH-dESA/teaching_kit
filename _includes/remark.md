# Easily create slideshow presentations from markdown with remark.js

## Intro to remark.js

Remark.js is a web based slideshow with some great features that is comparable to powerpoint or google slides except you can write your presentations entirely in [markdown](http://daringfireball.net/projects/markdown/syntax). 

You can see a [demo of remark.js in action here](http://remarkjs.com/) and when checking it out, be sure to press ```p``` to see the incredibly useful presenter mode.

## Useful features

- Presenter mode
- Markdown formatting
- Supports code/syntax highlighting
- Responsive
- Touch support (swipe to change slide)
- No special software required, just a browser
- Can be styled with CSS
- Is a portable, self-contained html document
- Works offline (with some caveats - more on this later)

## Focus on your content

Writing your presentation in a simple markdown document means you are freed from battling with the UI and layouts of individual slides and can **focus entirely on writing your content**.

By way of example, I wrote this post in markdown and converted it to remark.js by following these 5 steps:

## 1. Install markdown-to-slides via npm

    npm install markdown-to-slides -g

[https://github.com/partageit/markdown-to-slides](https://github.com/partageit/markdown-to-slides)

## 2. Create a custom CSS theme or use an existing one

Here's [an example of a basic remark.js theme](http://www.lendmeyourear.net/wp-content/uploads/remark-template-basic.css) that I created. You can use this as it is or edit it to your preference. Or you could skip this step entirely and just use the remark.js defaults which look fine. 

If you're using a custom CSS theme just store the CSS file somewhere handy on your computer because we'll be using it later when we convert our markdown file to a presentation.

## 3. Write your presentation in markdown.

You can write your presentation naturally like you would any other document in markdown but please take into consideration how your slides will be created. 

### Manually define new slides

You can manually insert horizontal lines which denote a new slide

    ### First slide heading
    
    First slide content
    
    ---

    ### Second slide heading
    
    Second slide content

### Use headings to denote new slides

You can use document-mode when converting your markdown document (more on this in the next step) which splits slides based on heading structure:

    # First slide
    
    ## Second slide
    
    ### Third slide
    
    Third slide content
    
    ### Fourth slide
    
    Fourth slide content

### Combination of lines and headings

You can also combine the two approaches for finer control. Simply use appropriate headings and insert lines in between larger blocks of text to break up slides.


### Slide notes

To write slide notes (visible in presenter mode) format your markdown like so:

    Slide content
   
    ???
    
    Slide notes


## 4. Convert markdown to presentation

    markdown-to-slides /path/to/slideshow.md -o /path/to/slideshow.html

### Document mode

Add the -d flag for document mode

    markdown-to-slides -d /path/to/slideshow.md -o /path/to/slideshow.html

Please note that when using document mode your headings must include a space after the markdown heading syntax otherwise it won't count as a heading and won't be converted into a new slide:

    ## Heading - works
    ##Heading - does not work 

### Custom CSS theme

Add the -s flag to use a custom CSS theme

    markdown-to-slides -s /path/to/remark-template.css /path/to/slideshow.md -o /path/to/slideshow.html


## 5. Open the resulting html file in your browser to see the results

```p``` opens presenter mode which shows you a preview of the next slide, a timer, and any slide notes you have written. 

```c``` will clone the slideshow in a separate tab for your viewers. The cloned slideshow changes slides along with you in presenter mode.

## More info

### Remark.js markdown extensions
There is a lot of useful markdown syntax specific to remark.js [found on their wiki](https://github.com/gnab/remark/wiki/Markdown)

### Offline images

Any images in your presentation that are hosted remotely will require an internet connection. you can get around this by placing any images in the same folder and referencing them locally in your markdown file e.g.

    ![Alt text](test.jpg) - markdown syntax
    
    <img src="test.jpg"> - html syntax
  

### Offline javascript

You need to cache the JavaScript in your browser by viewing your presentation with a working internet connection, then your presentation will work offline as long as that file is still cached.

---

To make it fully offline without depending on browser caching you can [grab the minified js](https://gnab.github.io/remark/downloads/remark-latest.min.js), store it in the same directory as your remark.js presentation and edit your presentation html document to replace

    <script src="http://gnab.github.io/remark/downloads/remark-latest.min.js"></script> 
    
With a reference to the local file

    <script src="remark-latest.min.js"></script>

### Custom css themes

Here's [an example of a basic remark.js theme](http://www.lendmeyourear.net/wp-content/uploads/remark-template-basic.css) which you can change to match your requirements.

### Custom fonts

You can use custom fonts in remark.js hosted on a remote CDN (such as google web fonts for example) or locally (stored in the same folder as the presentation perhaps) 

If you're willing to put in a bit more effort to make the theme as self contained as possible it's a good idea to convert your custom font to base64 using a service like [font squirrel](http://www.fontsquirrel.com/tools/webfont-generator). 

---

In the font squirrel tool you'll need to choose ```expert``` then go down to the CSS section and tick ```Base64 encode```. The zip file you download will contain a stylesheet.css file and all you need to do is copy the css the ```@font-face``` declaration into your remark.js theme file

    @font-face {
        font-family: 'my-cool-font';
        src: url(data:font/truetype;charset=utf-8;base64,<your-base64-encoded-string>) format('truetype');
    }

Then reference that font-family elsewhere in your css e.g.

    h1 { font-family: "my-cool-font"; }

### Using images in your theme

One possible use for images in your theme is to display your brand logo in a corner of every slide. 

Again, I suggest base64 encoding this image to make your theme truly portable and self-contained and avoid having to store image files alongside your presentation file. 

---

Encode your images using a service like [base64 image](http://www.base64-image.de/). The resulting base64 encoded string can be used in your theme like so

    .remark-slide-content:after {
        content: "";
        position: absolute;
        bottom: 10px;
        right: 10px;
        height: 40px;
        width: 120px;
        background-repeat: no-repeat;
        background-size: contain;
        background-image: url('data:image/png;base64,<your-base-64-encoded-string>');
    }

This will place the image in the bottom right corner of every slide. You can tweak the positional and size values to position it elsewhere.

## Conclusion
This way of creating presentations has turned something that used to be a chore into a process that is as easy as writing any document and really allows you to focus entirely on what you want to say rather than how each individual slide looks. Give it a try!


