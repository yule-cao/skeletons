const { defaults: tsjPreset } = require("ts-jest/presets");

module.exports = {
  rootDir: "src/test",
  transform: {
    ...tsjPreset.transform,
  },
};
