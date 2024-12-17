 /*eslint no-use-before-define: 2*/
module.exports = {
    root: true,
    env: {
      node: true,
      browser: true, // Add browser environment if applicable
    },
    extends: [
      'plugin:vue/essential', // or 'plugin:vue/vue3-essential' if using Vue 3
      'eslint:recommended',
    ],
    parserOptions: {
      parser: '@babel/eslint-parser',
      requireConfigFile: false, // Add this if you are using Babel parser
    },
    rules: {
      'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
      'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
      'vue/multi-word-component-names': 'off',
    },
  };
  
  