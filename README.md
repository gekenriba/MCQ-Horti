# HDO Prelims (Android)

A small Android app for APPSC Horticulture Development Officer (HDO) 2026 prelims practice. It has 10-question MCQ sets with explanations, memory hooks and notes on every option.

## Install on a phone

1. Open the latest release on this repo's **Releases** page on your Android phone.
2. Download `hdo-prelims.apk` and open it.
3. When Android asks, allow your browser or file manager to install unknown apps.
4. Open the app and tap **Turn on notifications** (or allow it after your first set).

Installing a newer version over the old one keeps your progress. Uninstalling erases it.

## Rules the app enforces

- Sets go in order, starting at Set 001.
- The next set unlocks 3 hours after you finish one, and the app notifies you when it opens.
- If a set is open and unfinished, you get a reminder every 3 hours.
- Your first tap on an option is final.
- Wrong answers collect under **Weak areas**.

## How new sets arrive

New sets are added to `data/sets.json` in this repo. The app downloads that file whenever it opens, so friends get new sets without reinstalling. Sets 001 onward are also bundled inside the app for offline use.

Questions are written by Claude from the 2026 syllabus and past APPSC papers. Anything whose source line says "verify" should be cross-checked with standard texts.

## Building

GitHub Actions builds a signed APK on every push that changes the app (`www/`, `android/`, config) and attaches it to a new release. Changes to `data/sets.json` alone do not trigger a build.

The signing key in `android/keystore/` is a sideload-only key kept in the repo so every build can update the previous one. Don't reuse it for anything else.
