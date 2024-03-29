#!/usr/bin/python
# -*- coding: utf-8  -*-

cssdiff="""<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style type="text/css">
table.diff, td.diff-otitle, td.diff-ntitle {
    background-color: white;
}
td.diff-otitle,
td.diff-ntitle {
    text-align: center;
}
td.diff-marker {
    text-align: right;
}
.rtl td.diff-marker {
    text-align: left;
}
td.diff-lineno {
    font-weight: bold;
}
td.diff-addedline {
    background: #e4f6d8;
    font-size: smaller;
}
td.diff-deletedline {
    background: #d8e4f6;
    font-size: smaller;
}
td.diff-context {
    background: #eee;
    font-size: smaller;
}
.diffchange {
    color: red;
    font-weight: bold;
    text-decoration: none;
    white-space: pre-wrap;
    white-space: -moz-pre-wrap;
}

table.diff {
    border: none;
    width: 98%;
    border-spacing: 4px;
    
    /* Fixed layout is required to ensure that cells containing long URLs
       don't widen in Safari, Internet Explorer, or iCab */
    table-layout: fixed;
}
table.diff td {
    padding: 0;
}
table.diff col.diff-marker {
    width: 2%;
}
table.diff col.diff-content {
    width: 48%;
}
table.diff td div {
    /* Force-wrap very long lines such as URLs or page-widening char strings.
       CSS 3 draft..., but Gecko doesn't support it yet:
       https://bugzilla.mozilla.org/show_bug.cgi?id=99457 */
    word-wrap: break-word;
    
    /* As fallback, scrollbars will be added for very wide cells
       instead of text overflowing or widening */
    overflow: auto;
    
    /* The above rule breaks on very old versions of Mozilla due
       to a bug which collapses the table cells to a single line.
       
       In Mozilla 1.1 and below with JavaScript enabled, the rule
       will be overridden with this by diff.js; wide cell contents
       then spill horizontally without widening the rest of the
       table: */
    /* overflow: visible; */
}

/*
 * Styles for the HTML Diff
 */
div.diff-switchtype{
    text-align: center;
    font-weight: bold;
    font-size: smaller;
}

span.diff-html-added {
  font-size: 100%;
  background-color: #20ff20
}

span.diff-html-removed {
  font-size: 100%;
  text-decoration: line-through;
  background-color: #ff2020
}

span.diff-html-changed {
  background: url(images/diffunderline.gif) bottom repeat-x;
  *background-color: #c6c6fd; /* light blue */
}

span.diff-html-added img{
 border: 5px solid #ccffcc;
}

span.diff-html-removed img{
 border: 5px solid #fdc6c6;
}

span.diff-html-changed img{
 border: 5px dotted #000099;
 
}

span.diff-html-changed  {
  position: relative;   /* this is key */
  cursor: help;
}
 
span.diff-html-changed span.tip {
  display: none;        /* so is this */
}

/* tooltip will display on :hover event */
 
span.diff-html-changed:hover span.tip {
  display: block;
  z-index: 95;
  position: absolute;
  top: 2.5em;
  left: 0;
  width: auto;
  line-height: 1.2em;
  padding: 3px 7px 4px 6px;
  border: 1px solid #336;
  background-color: #f7f7ee;
  font-size: 10px;
  text-align: left;
}
</style>
</head><body>"""
