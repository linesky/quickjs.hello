import os
import subprocess

# Lista de registradores
registers = ["#0","r0","r1","r2","r3","r4","r5","r6","r7","r8","[r0]","[r1]","[r2]","[r3]","[r4]","[r5]","[r6]","[r7]","[r8]"]

# Lista de instruções
instructions = ["adc",
"cmp","mov", "add","sub",
"and", "or","xor","in","out","int","bcxz","becxz","b","bcc","ret","neg","not","push","rcl","rcr","rol","sal",
"sar","sbb","set","shl","shr","str","sub",
"test","xchg","xor","int","inc","dec","mul","umul","idiv","udiv","aaa","nop"
"outb","outw","outd","popa","popw","popd","popf","popfw","popfd","pusha","pushf","bne","be","bnz","bz","bg","bl","blt","beq",""]

# Valor para a operação
value = "0x10"

# Caminho dos arquivos temporários
asm_file = "/tmp/out.asm"
bin_file = "/tmp/outs"
bin_file2 = "/tmp/out"
output_file = "out.txt"
loo=len(instructions)
i100=100/loo
lcounts=0
# Limpar o arquivo de saída
with open(output_file, "w") as f:
    f.write("")
# Função para gerar o arquivo assembly, compilar e testar
def generate_assembly_and_test3(instruction):
    # Gerar o conteúdo do arquivo .asm
    asm_content = f".global my\nmy:\n{instruction} \n"
    
    # Escrever o arquivo assembly
    with open(asm_file, "w") as asm:
        asm.write(asm_content)
    nasm_command = f'printf "{instruction} | " >> out.txt'
    nasm_result = subprocess.run(nasm_command, shell=True)
    # Executar o NASM e redirecionar saída para out.txt
    # Executar o NASM e redirecionar saída para out.txt
    nasm_command = f"/bin/arm-none-eabi-as {asm_file} -o {bin_file2} >> {output_file} 2>&1"
    nasm_result = subprocess.run(nasm_command, shell=True)
    nasm_command = f"/bin/arm-none-eabi-objcopy {bin_file2} -O binary  {bin_file}   >> {output_file} 2>&1"
    nasm_result = subprocess.run(nasm_command, shell=True)

 # Verificar se houve erro no NASM
    if nasm_result.returncode == 0:
        # Se compilou corretamente, gerar o hexdump do binário com xxd
        f1=open(f"{bin_file}","rb")
        sss=f1.read()
        f1.close()
        s=""
        for b in sss:
            s=s+f"{b:02x}"
        s=s+"\n"
        with open(output_file, "a") as asm:
            asm.write(s)

# Função para gerar o arquivo assembly, compilar e testar
def generate_assembly_and_test2(instruction, register):
    # Gerar o conteúdo do arquivo .asm
    asm_content = f".global my\nmy:\n{instruction} {register}\n"
    
    # Escrever o arquivo assembly
    with open(asm_file, "w") as asm:
        asm.write(asm_content)
    nasm_command = f'printf "{instruction} {register} | " >> out.txt'
    nasm_result = subprocess.run(nasm_command, shell=True)
    # Executar o NASM e redirecionar saída para out.txt
    nasm_command = f"/bin/arm-none-eabi-as {asm_file} -o {bin_file2} >> {output_file} 2>&1"
    nasm_result = subprocess.run(nasm_command, shell=True)
    nasm_command = f"/bin/arm-none-eabi-objcopy {bin_file2} -O binary  {bin_file}   >> {output_file} 2>&1"
    nasm_result = subprocess.run(nasm_command, shell=True)
 # Verificar se houve erro no NASM
    if nasm_result.returncode == 0:
        # Se compilou corretamente, gerar o hexdump do binário com xxd
        f1=open(f"{bin_file}","rb")
        sss=f1.read()
        f1.close()
        s=""
        for b in sss:
            s=s+f"{b:02x}"
        s=s+"\n"
        with open(output_file, "a") as asm:
            asm.write(s)

# Função para gerar o arquivo assembly, compilar e testar
def generate_assembly_and_test(instruction, register, value):
    # Gerar o conteúdo do arquivo .asm
    asm_content = f".global my\nmy:\n{instruction} {register},{value}\n"
    
    # Escrever o arquivo assembly
    with open(asm_file, "w") as asm:
        asm.write(asm_content)
    nasm_command = f'printf "{instruction} {register},{value}|" >> out.txt'
    nasm_result = subprocess.run(nasm_command, shell=True)
    # Executar o NASM e redirecionar saída para out.txt
    
    nasm_command = f"/bin/arm-none-eabi-as {asm_file} -o {bin_file2} >> {output_file} 2>&1"
    nasm_result = subprocess.run(nasm_command, shell=True)
    nasm_command = f"/bin/arm-none-eabi-objcopy {bin_file2} -O binary   {bin_file}  >> {output_file} 2>&1"
    nasm_result = subprocess.run(nasm_command, shell=True)

# Verificar se houve erro no NASM
    if nasm_result.returncode == 0:
        # Se compilou corretamente, gerar o hexdump do binário com xxd
        f1=open(f"{bin_file}","rb")
        sss=f1.read()
        f1.close()
        s=""
        for b in sss:
            s=s+f"{b:02x}"
        s=s+"\n"
        with open(output_file, "a") as asm:
            asm.write(s)
print("keywords:"+str(loo))
print("advaced:"+str(i100))
# Testar todas as combinações de instruções e registradores
for instruction in instructions:
    print(str(lcounts*i100)+" %")
    
    generate_assembly_and_test3(instruction)
    lcounts+=1
    for register in registers:
        generate_assembly_and_test2(instruction, register)
        for register2 in registers:
            generate_assembly_and_test(instruction, register,register2)

# Abrir o arquivo final com gedit
subprocess.run(f"gedit {output_file}", shell=True)

