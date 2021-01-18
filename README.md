# vue3-heroicons

Heroicons components for Vue 3 with TypeScript typings.

Version of this package will follow the Heroicons versions.

## Usage

```
yarn add @havekes/vue3-heroicons
```

In a component

```js
// ...
import { OPlus } from '@havekes/vue3-heroicons';

export default defineComponent({
  components: { OPlus }
  // ...
})
```

## Updating from upstream and compiling

The `make_library.py` script will regenerate all icons from the [heroicons repo](https://github.com/tailwindlabs/heroicons).
It requires the request Python package to be installed.

```
pip install requests
python make_library.py
yarn build
```