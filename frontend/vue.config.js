module.exports = {
  configureWebpack: {
    devServer: {
      proxy: 'http://localhost:8009',
      allowedHosts: ['all', 'localhost', 'auto', 'fastapi.kube.zz'],
//      watchOptions: {
//        ignored: [/\.#/],
//      },
    },
  },
};
