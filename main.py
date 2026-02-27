import tkinter as tk
from tkinter import messagebox

# ===== CONFIG DO ATIVO =====
DOLLARS_PER_POINT_PER_LOT = 1.0  # US30 FTMO


def calcular():
    try:
        balance = float(entry_balance.get())
        risk_percent = float(entry_risk.get())
        stop_points = float(entry_stop.get())
        daily_loss_percent = float(entry_daily_loss.get())

        if balance <= 0 or risk_percent <= 0 or stop_points <= 0 or daily_loss_percent <= 0:
            raise ValueError

        # Risco em $
        risk_dollars = balance * (risk_percent / 100)

        # Lote ideal
        lotes = risk_dollars / (stop_points * DOLLARS_PER_POINT_PER_LOT)

        # $ por ponto
        dollars_per_point = lotes * DOLLARS_PER_POINT_PER_LOT

        # % da conta por ponto
        percent_per_point = (dollars_per_point / balance) * 100

        # Daily loss em $
        daily_loss_dollars = balance * (daily_loss_percent / 100)

        # Quantos trades podem ser perdidos
        max_losses = daily_loss_dollars / risk_dollars

        resultado.set(
            f"Risco por trade: ${risk_dollars:.2f}\n"
            f"Lote ideal: {lotes:.2f}\n"
            f"$ por ponto: ${dollars_per_point:.2f}\n"
            f"% da conta por ponto: {percent_per_point:.4f}%\n\n"
            f"Daily Loss Máx: ${daily_loss_dollars:.2f}\n"
            f"Trades perdedores possíveis: {max_losses:.1f}"
        )

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Preencha todos os campos com números válidos maiores que zero."
        )


# ===== GUI =====
root = tk.Tk()
root.title("Alysson é gay – Risk & Position Calculator")
root.geometry("420x360")
root.resizable(False, False)

tk.Label(root, text="Balance ($)", font=("Arial", 10)).pack(pady=4)
entry_balance = tk.Entry(root, font=("Arial", 10))
entry_balance.pack()

tk.Label(root, text="Risco por trade (%)", font=("Arial", 10)).pack(pady=4)
entry_risk = tk.Entry(root, font=("Arial", 10))
entry_risk.pack()

tk.Label(root, text="Stop (pontos)", font=("Arial", 10)).pack(pady=4)
entry_stop = tk.Entry(root, font=("Arial", 10))
entry_stop.pack()

tk.Label(root, text="Daily Loss Máx (%)", font=("Arial", 10)).pack(pady=4)
entry_daily_loss = tk.Entry(root, font=("Arial", 10))
entry_daily_loss.pack()

tk.Button(
    root,
    text="Calcular",
    command=calcular,
    font=("Arial", 10),
    bg="#1f6aa5",
    fg="white",
    width=25
).pack(pady=15)

resultado = tk.StringVar()
tk.Label(
    root,
    textvariable=resultado,
    font=("Arial", 10),
    justify="left"
).pack(pady=10)

root.mainloop()
