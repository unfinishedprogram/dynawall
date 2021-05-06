# Nececary configs
## Awesome WM

- Must add these rules to ```auful.rules``` in rc.lua config file

```
{ rule_any = {
        class = {
            "dynamicwall1", "dynamicwall2",
            "dynamicwall3", "dynamicwall4",
            "dynamicwall5", "dynamicwall6",
            "dynamicwall7", "dynamicwall8",
            "dynamicwall9", "dynamicwall10"
        } 
    }, 
    properties = { 
        maximized_vertical = true, maximized_horizontal = true,
        border_width = 0,
        focus = false,
        focusable = false,
        below = true,
        sticky = true,
        floating = true,
    } 
},

{ rule = { class = "dynamicwall1" }, properties = { screen = 1 } },
{ rule = { class = "dynamicwall2" }, properties = { screen = 2 } },
{ rule = { class = "dynamicwall3" }, properties = { screen = 3 } },
{ rule = { class = "dynamicwall4" }, properties = { screen = 4 } },
{ rule = { class = "dynamicwall5" }, properties = { screen = 5 } },
{ rule = { class = "dynamicwall6" }, properties = { screen = 6 } },
{ rule = { class = "dynamicwall7" }, properties = { screen = 7 } },
{ rule = { class = "dynamicwall8" }, properties = { screen = 8 } },
{ rule = { class = "dynamicwall9" }, properties = { screen = 9 } },
{ rule = { class = "dynamicwall10" }, properties = { screen = 10 } },
```

- To initalize the wallpaper add this at the end of your awesome config file:
mon1, mon2, mon3... represent the indexes of your monitors, 
normaly these will be indexed sequentialy starting at 1
Add the indexes of each monitor where you want the dynamic wallpaper

```awful.spawn.with_shell("bash [PATH-TO dynawallinit.sh] [mon1] [mon2] [mon3]...")```

### ex:

```awful.spawn.with_shell("bash ~/.dynawall/dynawallinit.sh] 1 2 3```