import wave
import numpy as np

# Parámetros del audio
sample_rate = 44100  # Tasa de muestreo
bip_duration = 0.2  # Duración de cada "bip" en segundos
silence_duration = 0.2  # Duración del silencio entre "bips"
frequency = 440  # Frecuencia del "bip" (Hz)

# Clave para decodificar (1 bip = A, 2 bips = B, etc.)
decode_key = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
    6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J'
    # Agrega más si lo necesitas
}

# Mensaje a codificar (por ejemplo, 'ABC' -> 1 bip, 2 bips, 3 bips)
message = "CAB"

# Genera un tono de "bip"
def generate_bip(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * t * 2 * np.pi)
    return tone

# Genera la señal de audio para el mensaje
audio_signal = []

for char in message:
    # Encuentra cuántos "bips" corresponden al carácter
    bip_count = list(decode_key.values()).index(char) + 1
    
    # Añade los "bips"
    for _ in range(bip_count):
        audio_signal.append(generate_bip(frequency, bip_duration, sample_rate))
        # Añade un pequeño silencio entre "bips"
        silence = np.zeros(int(sample_rate * silence_duration))
        audio_signal.append(silence)

# Convertir la señal a un formato compatible para guardar
audio_signal = np.concatenate(audio_signal) * 32767  # Normalización
audio_signal = audio_signal.astype(np.int16)  # Convertir a entero de 16 bits

# Guardar el archivo WAV
with wave.open("bip_code.wav", "w") as wav_file:
    wav_file.setnchannels(1)  # Mono
    wav_file.setsampwidth(2)  # 2 bytes (16 bits)
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(audio_signal.tobytes())

print("Archivo de audio generado: bip_code.wav")
