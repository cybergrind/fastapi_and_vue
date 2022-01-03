module.exports = {
  configureWebpack: {
    devServer: {
      allowedHosts: ['all', 'localhost', 'auto', 'fastapi.kube.zz'],
      watchOptions: {
        ignored: [/\.#/],
      },
    },
  },
};
