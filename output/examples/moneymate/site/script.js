const currency = new Intl.NumberFormat("ko-KR", {
  style: "currency",
  currency: "KRW",
  maximumFractionDigits: 0,
});

const appState = {
  budgetLimit: 2500000,
  expenses: [
    { title: "점심 미팅", category: "식비", amount: 28000, date: "2026-03-06" },
    { title: "Figma 구독", category: "구독", amount: 24000, date: "2026-03-05" },
    { title: "택시 이동", category: "교통", amount: 19800, date: "2026-03-05" },
    { title: "광고 소재 구매", category: "업무", amount: 56000, date: "2026-03-04" },
    { title: "저녁 식사", category: "식비", amount: 42000, date: "2026-03-03" },
  ],
};

function setupTabs() {
  const chips = document.querySelectorAll("[data-tab]");
  const panels = document.querySelectorAll("[data-panel]");
  const shortcuts = document.querySelectorAll("[data-tab-target]");

  function activate(tab) {
    chips.forEach((chip) => chip.classList.toggle("is-active", chip.dataset.tab === tab));
    panels.forEach((panel) => panel.classList.toggle("is-active", panel.dataset.panel === tab));
  }

  chips.forEach((chip) => {
    chip.addEventListener("click", () => activate(chip.dataset.tab));
  });

  shortcuts.forEach((button) => {
    button.addEventListener("click", () => activate(button.dataset.tabTarget));
  });
}

function calculateSpent() {
  return appState.expenses.reduce((sum, item) => sum + item.amount, 1372200);
}

function renderSummary() {
  const spent = calculateSpent();
  const remaining = appState.budgetLimit - spent;
  const remainingEl = document.getElementById("remaining-budget");
  const spentEl = document.getElementById("spent-total");
  const previewEl = document.getElementById("budget-preview-value");
  const paceCopyEl = document.getElementById("pace-copy");

  if (remainingEl) remainingEl.textContent = currency.format(remaining);
  if (spentEl) spentEl.textContent = currency.format(spent);
  if (previewEl) previewEl.textContent = currency.format(remaining);

  if (paceCopyEl) {
    paceCopyEl.textContent =
      remaining > 700000
        ? "지금 속도면 예산 범위 안에서 마감할 가능성이 높습니다."
        : "지출 속도가 빨라졌습니다. 이번 주는 식비와 구독 점검이 필요합니다.";
  }
}

function renderExpenses() {
  const list = document.getElementById("expense-list");
  if (!list) return;

  list.innerHTML = "";
  [...appState.expenses]
    .sort((a, b) => (a.date < b.date ? 1 : -1))
    .slice(0, 6)
    .forEach((item) => {
      const row = document.createElement("article");
      row.className = "expense-item";
      row.innerHTML = `
        <div>
          <strong>${item.title}</strong>
          <span>${item.category} · ${item.date}</span>
        </div>
        <em>${currency.format(item.amount)}</em>
      `;
      list.appendChild(row);
    });
}

function setupExpenseForm() {
  const form = document.getElementById("expense-form");
  const hint = document.getElementById("form-hint");
  if (!form) return;

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const title = document.getElementById("expense-title").value.trim();
    const category = document.getElementById("expense-category").value;
    const amount = Number(document.getElementById("expense-amount").value);
    const date = document.getElementById("expense-date").value;

    if (!title || !amount || amount < 1000) {
      hint.textContent = "항목명과 1,000원 이상의 금액을 입력하세요.";
      return;
    }

    appState.expenses.push({ title, category, amount, date });
    renderExpenses();
    renderSummary();
    form.reset();
    document.getElementById("expense-amount").value = "18000";
    document.getElementById("expense-date").value = "2026-03-08";
    hint.textContent = `"${title}" 지출이 추가되었습니다. 대시보드 수치를 갱신했습니다.`;
  });
}

function setupBudgetForm() {
  const form = document.getElementById("budget-form");
  const input = document.getElementById("budget-limit");
  if (!form || !input) return;

  input.addEventListener("input", () => {
    const preview = document.getElementById("budget-preview-value");
    const nextBudget = Number(input.value || 0);
    const previewRemaining = nextBudget - calculateSpent();
    if (preview) preview.textContent = currency.format(previewRemaining);
  });

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    appState.budgetLimit = Number(input.value || appState.budgetLimit);
    renderSummary();
  });
}

document.addEventListener("DOMContentLoaded", () => {
  setupTabs();
  renderSummary();
  renderExpenses();
  setupExpenseForm();
  setupBudgetForm();
});
