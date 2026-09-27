/* Tia Clara — JS mínimo e opcional.
   Sem este arquivo (ou com JS desligado), a lista de navegação do cabeçalho
   fica sempre visível e empilhada: o site funciona sem JavaScript.
   Com JS, o botão "Menu" passa a abrir/fechar a lista (classe .tc-js no <html>
   já foi ligada por um script inline no <head>, antes deste arquivo carregar). */
(function () {
  "use strict";

  var menu = document.getElementById("tc-menu");
  if (!menu) return;
  var botao = menu.querySelector(".tc-menu__botao");
  var lista = menu.querySelector(".tc-menu__lista");
  if (!botao || !lista) return;
  var veu = document.querySelector(".tc-menu__veu");

  function fechar() {
    menu.setAttribute("data-aberto", "false");
    botao.setAttribute("aria-expanded", "false");
    if (veu) veu.hidden = true;
  }
  function alternar() {
    var aberto = menu.getAttribute("data-aberto") === "true";
    menu.setAttribute("data-aberto", aberto ? "false" : "true");
    botao.setAttribute("aria-expanded", aberto ? "false" : "true");
    if (veu) veu.hidden = aberto;
  }

  fechar();
  botao.addEventListener("click", alternar);

  lista.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", fechar);
  });

  document.addEventListener("keydown", function (evento) {
    if (evento.key === "Escape" && menu.getAttribute("data-aberto") === "true") {
      fechar();
      botao.focus();
    }
  });

  document.addEventListener("click", function (evento) {
    if (menu.getAttribute("data-aberto") === "true" && !menu.contains(evento.target)) fechar();
  });
})();
