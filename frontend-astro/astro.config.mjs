import { defineConfig } from 'astro/config';

const postprocess = {
    name: 'postprocess',
    enforce: 'post',
    transform(src, _) {
        src = src.replace(/\(\(([^)]*)\)\)/g, "{{$1}}");

        process.env.NODE_ENV === 'development'
            ? src = src.replace(/\(%([^%]*)%\)/g, "")
            : src = src.replace(/\(%([^%]*)%\)/g, "{%$1%}");


        if (process.env.NODE_ENV === 'production') {
            src = src.replace(/\/public\//g, "/");
        }
        
        return {
            code: src,
            map: null
        }
    }
}

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [ postprocess ]
  },
  build: {
    assets: 'static'
  }
});
