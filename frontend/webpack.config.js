module.exports = {
    resolve: {
        // extensions: ['.tsx', '.ts', '.js'],
      //   fallback: { "http": false, "browser": false, "https": false, 
      //     "stream": false, "url": false, "buffer": false, "timers": false
      //   }
      // }
    resolve: {
        fallback: { "path": require.resolve("path-browserify") ,"zlib": require.resolve("browserify-zlib"), "crypto": require.resolve("crypto-browserify"),
        "stream": require.resolve("stream-browserify"), "http": require.resolve("stream-http")  }
    }
  }
}