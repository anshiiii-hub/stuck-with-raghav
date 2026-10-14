# stuck-with-raghav

A birthday gift for a friend: a playful, single-page "annual review" web app that teases him affectionately and ends with a sincere letter.

## What's inside

It opens with a retro terminal boot screen, then walks through seven pages with previous/next buttons:

1. An intro with a birthday candle to click.
2. A football-style trading card with stats and a scouting report.
3. A "combat record" with a health bar and buttons that damage or heal.
4. A mock video-review screen that runs a fake analysis and delivers a verdict.
5. A timeline of the friendship.
6. A random excuse generator, and a checkbox that dodges your cursor.
7. A final letter whose lines fade in as you scroll.

Along the way: a tilt-on-hover card effect, click particles, sound effects, random pop-up roasts, and draggable sticky notes. It works with touch on mobile too. The look starts dark with neon green and gold, then turns warm and handwritten for the final letter.

## Tech

- **Backend:** Python and Flask, serving a single template.
- **Frontend:** vanilla JavaScript, [Tailwind CSS](https://tailwindcss.com/), [GSAP](https://gsap.com/) for animation, [Tone.js](https://tonejs.github.io/) for synthesized sound, Font Awesome icons and Google Fonts.

The libraries and fonts load from CDNs, so you need an internet connection.

## Run it locally

```bash
git clone https://github.com/anshiiii-hub/stuck-with-raghav.git
cd stuck-with-raghav
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5001.
