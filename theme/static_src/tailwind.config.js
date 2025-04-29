/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  darkMode: ["class"],
  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    "../templates/**/*.html",

    /*
     * Main templates directory of the project (BASE_DIR/templates).
     * Adjust the following line to match your project structure.
     */
    "../../templates/**/*.html",

    /*
     * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
     * Adjust the following line to match your project structure.
     */
    "../../**/templates/**/*.html",

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
     * patterns match your project structure.
     */
    /* JS 1: Ignore any JavaScript in node_modules folder. */
    // '!../../**/node_modules',
    /* JS 2: Process all JavaScript files in the project. */
    // '../../**/*.js',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  theme: {
    extend: {
      fontSize: {
        "fluid-00": "clamp(.50rem, 2vw, 1rem)",
        "fluid-0": "clamp(.75rem, 2vw, 1rem)",
        "fluid-base": "clamp(1.125rem, 3vw, 1.5rem)",
        "fluid-1": "clamp(1rem, 4vw, 1.5rem)",
        "fluid-2": "clamp(1.5rem, 6vw, 2.5rem)",
        "fluid-3": "clamp(2rem, 9vw, 3.5rem)",
        "fluid-4": "clamp(2rem, 4vw, 3rem)",
        "fluid-5": "clamp(4rem, 5vw, 5rem)",
        "fluid-6": "clamp(5rem, 7vw, 7.5rem)",
        "fluid-7": "clamp(7.5rem, 10vw, 10rem)",
        "fluid-8": "clamp(10rem, 20vw, 15rem)",
        "fluid-9": "clamp(15rem, 30vw, 20rem)",
        "fluid-10": "clamp(20rem, 40vw, 30rem)",
      },
    },
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/aspect-ratio"),
  ],
};
