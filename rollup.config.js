// import our third party plugins
import VuePlugin from "rollup-plugin-vue";
import typescript from "@rollup/plugin-typescript";
import pkg from "./package.json"; // import our package.json file to re-use the naming

export default {
  // this is the file containing all our exported components/functions
  input: "lib/index.ts",
  // this is an array of outputed formats
  output: [
    {
      file: pkg.module, // the name of our esm library
      format: "esm", // the format of choice
      sourcemap: true, // ask rollup to include sourcemaps
    },
  ],
  // this is an array of the plugins that we are including
  plugins: [typescript(), VuePlugin()],
  // ask rollup to not bundle Vue in the library
  external: ["vue"],
};
