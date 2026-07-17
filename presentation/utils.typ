#import "slide.typ": jump, meanwhile, pause, setup, theme
#import "@preview/octique:0.1.1": octique-inline

#let colors = theme.colors
#let primary = colors.primary
#let muted = rgb("#6f6263")
#let pale = rgb("#f8eeee")
#let green = rgb("#2f735c")
#let amber = rgb("#a86613")

#let note-box(title, body) = block(
    width: 100%,
    inset: (x: 0.75em, y: 0.55em),
    fill: rgb("#fbf4f5"),
    stroke: (left: 4pt + primary, rest: 0.6pt + colors.primary-muted),
    radius: 4pt,
    {
        text(fill: primary, weight: "bold", title)
        parbreak()
        body
    },
)

#let pill(body, fill: pale, ink: primary) = box(
    inset: (x: 0.5em, y: 0.2em),
    radius: 99pt,
    fill: fill,
    text(size: 14pt, weight: "bold", fill: ink, body),
)

#let card(title, body, accent: primary, width: 100%) = block(
    width: width,
    inset: (x: 0.7em, y: 0.5em),
    radius: 6pt,
    fill: accent.lighten(80%),
    stroke: (left: 4pt + accent, rest: 0.5pt + accent.lighten(60%)),
    {
        text(size: 17pt, weight: "bold", fill: accent, title)
        parbreak()
        align(left, text(size: 15pt, body))
    },
)

#let flow-node(title, body, accent: primary) = block(
    width: 100%,
    inset: 0.5em,
    radius: 6pt,
    fill: accent.lighten(89%),
    stroke: 1pt + accent.lighten(45%),
    align(center, {
        text(size: 16pt, weight: "bold", fill: accent, title)
        parbreak()
        text(size: 13pt, body)
    }),
)
