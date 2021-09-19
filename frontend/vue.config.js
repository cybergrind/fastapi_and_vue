module.exports = {
  configureWebpack: {
    devServer: {
      watchOptions: {
        ignored: [/\.#/],
      },
    },
  },
};
