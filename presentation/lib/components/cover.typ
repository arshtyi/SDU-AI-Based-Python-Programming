#import "../foundation/theme.typ": theme
#import "../utils/draw.typ": place-circle

/// Renders the opening cover page.
///
/// The cover uses the SDU and SDU CS logos, decorative circles, and the theme's
/// cover font and color tokens. It also resets the page counter so the first
/// content slide starts from page 1.
///
/// - title (str): Main title shown in the center of the cover.
/// - subtitle (str): Subtitle shown below the title.
/// - author (str): Author name shown in the lower badge.
/// - term (str): Course term shown in the lower badge.
/// -> content
#let render-cover(
    title: "SDU OS Slide",
    subtitle: "Slide for SDU OS",
    author: "arshtyi",
    term: "2026 Spring",
) = {
    let fonts = theme.fonts
    let colors = theme.colors

    set text(
        font: fonts.cover,
        weight: "bold",
    )
    set page(foreground: {
        place(
            dx: 0.77cm,
            dy: 1.19cm,
            image("../../assets/sdu.png", width: 10.82cm, height: 2.86cm),
        )
        let cover-circle = place-circle.with(stroke: none)
        cover-circle(
            12.59cm + 1.62cm / 2,
            -0.87cm + 1.62cm / 2,
            1.62cm / 2,
            fill: colors.neutral,
        )
        cover-circle(
            26.98cm + 31.3cm / 2,
            -6.12cm + 31.3cm / 2,
            31.3cm / 2,
            fill: colors.primary,
        )
        cover-circle(
            1.59cm + 3.56cm / 2,
            17.27cm + 3.56cm / 2,
            3.56cm / 2,
            fill: colors.primary,
        )
        cover-circle(
            1.59cm + 3.56cm / 2,
            17.27cm + 3.56cm / 2,
            2.4cm / 2,
            fill: white,
        )
    })
    place(
        dx: 1.48cm,
        dy: 6.81cm,
        block(
            width: 24.32cm,
            height: 4.36cm,
            inset: 25pt,
            {
                set align(center)
                set par(leading: 2.6em)
                text(size: 40pt, title)
                linebreak()
                text(size: 32pt, subtitle)
            },
        ),
    )
    place(
        dx: 5.46cm,
        dy: 13.49cm,
        block(
            width: 6.77cm,
            height: 1.13cm,
            radius: 50pt,
            fill: colors.primary,
            align(
                center + horizon,
                text(
                    size: 20pt,
                    fill: white,
                    "Author: " + author,
                ),
            ),
        ),
    )
    place(
        dx: 12.87cm,
        dy: 13.49cm,
        block(
            width: 8.49cm,
            height: 1.13cm,
            radius: 50pt,
            fill: colors.neutral-soft,
            align(
                center + horizon,
                text(
                    size: 20pt,
                    fill: black,
                    "Term: " + term,
                ),
            ),
        ),
    )
    counter(page).update(0)
}
