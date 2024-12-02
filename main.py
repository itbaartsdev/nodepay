import os
import sys
from rich.console import Console
from rich.theme import Theme
import subprocess

# Konfigurasi tema kustom
custom_theme = Theme({
    "info": "#00c8ff",     # Biru cerah
    "warning": "#ffb86c",  # Orange
    "error": "#ff5555",    # Merah
    "success": "#50fa7b",  # Hijau
    "title": "#bd93f9",    # Ungu
    "header": "#8be9fd"    # Cyan
})

# Setup console dengan tema
console = Console(theme=custom_theme)

def clear():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    clear()
    console.print("\n[bold cyan]NODEPAY AI AUTOMATION[/bold cyan]")
    console.print("[cyan]" + "─" * 45 + "[/cyan]")
    console.print("[cyan]Author  : [/cyan][white]ITBAARTS[/white]")
    console.print("[cyan]Version : [/cyan][white]5.1.12[/white]")
    console.print("[cyan]" + "─" * 45 + "[/cyan]\n")

def display_menu():
    console.print("[bold cyan]Pilih versi yang ingin dijalankan:[/bold cyan]")
    console.print("[cyan]1.[/cyan] Premium Version")
    console.print("[cyan]2.[/cyan] Free Version")
    console.print("[cyan]3.[/cyan] Keluar")
    console.print("\n[cyan]" + "─" * 45 + "[/cyan]")

def run_script(script_name):
    try:
        subprocess.run([sys.executable, script_name], check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error menjalankan script: {e}[/red]")
    except FileNotFoundError:
        console.print(f"[red]File {script_name} tidak ditemukan![/red]")

def main():
    while True:
        display_header()
        display_menu()
        
        try:
            choice = input("\n[?] Masukkan pilihan (1-3): ")
            
            if choice == "1":
                clear()
                run_script("premium.py")
                input("\nTekan Enter untuk kembali ke menu...")
            
            elif choice == "2":
                clear()
                run_script("free.py")
                input("\nTekan Enter untuk kembali ke menu...")
            
            elif choice == "3":
                console.print("\n[cyan]Terima kasih telah menggunakan program ini![/cyan]")
                break
            
            else:
                console.print("\n[red]Pilihan tidak valid! Silakan pilih 1-3.[/red]")
                input("\nTekan Enter untuk melanjutkan...")
                
        except KeyboardInterrupt:
            console.print("\n[yellow]Program dihentikan oleh user[/yellow]")
            break
        except Exception as e:
            console.print(f"\n[red]Terjadi kesalahan: {str(e)}[/red]")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Program dihentikan oleh user[/yellow]")
    except Exception as e:
        console.print(f"\n[red]Error: {str(e)}[/red]")
    finally:
        console.print("\n[cyan]" + "─" * 50 + "[/cyan]")
