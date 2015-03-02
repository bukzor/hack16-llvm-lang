var eval_hilang = function(source) {
  // http://kripken.github.io/emscripten-site/docs/porting/connecting_cpp_and_javascript/Interacting-with-code.html#calling-compiled-c-functions-from-javascript-using-ccall-cwrap
  ptr = allocate(intArrayFromString(source), 'i8', ALLOC_STACK);
  getCFunc('eval_hilang')(ptr);
};


langPlugin.runLang(eval_hilang, 'application/x-hilang');
