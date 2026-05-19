const now = new Date();
const formatted = now.toLocaleDateString(undefined, {
  weekday: "long",
  month: "long",
  day: "numeric",
});

document.documentElement.style.scrollBehavior = "smooth";
console.log(`Portfolio website loaded on ${formatted}`);
