# RULER COLUMN

A Sublime Text plugin that shows ruler columns only on lines where the text overflows.

`Menu > Preferences > Settings`:

```json
{
    "ruler_column": 80
}
```

In newer versions of Sublime Text (`~= 3154`) customising the color of the ruler column is straight forward enough.

Create a color scheme override in your Sublime Text User directory (find the User directory via `Menu > Preferences > Browse Packages...`).

Name the override file the same as your color scheme e.g. for the [MonokaiFree](https://github.com/gerardroche/sublime-monokai-free) color scheme it would be `MonokaiFree.sublime-color-scheme`.

```
{
    "rules":
    [
        {
            "scope": "ruler.column",
            "background": "#e6db74",
            "foreground": "#272822"
        }
    ]
}
```
