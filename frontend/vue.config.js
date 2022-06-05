module.exports = {
  configureWebpack: {
    devServer: {
      proxy: {
        '^/api': {
          target: 'http://localhost:8009',
          ws: true,
          changeOrigin: true,
        }
      },
      allowedHosts: ['all', 'localhost', 'auto', 'fastapi.kube.zz'],
//      watchOptions: {
//        ignored: [/\.#/],
//      },
    },
  },
};
