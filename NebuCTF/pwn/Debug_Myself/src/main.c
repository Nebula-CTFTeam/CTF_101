#include <stdio.h>
#include <string.h>

#define COLOR_RED "\033[31m"
#define COLOR_GREEN "\033[32m"
#define COLOR_YELLOW "\033[33m"
#define COLOR_BLUE "\033[34m"
#define COLOR_MAGENTA "\033[35m"
#define COLOR_CYAN "\033[36m"
#define COLOR_RESET "\033[0m"

size_t tmp_bp, tmp_sp, tmp_rdi;

void pop_rdi_ret() {
    __asm__("pop rdi; ret");
}
void pop_rdx_ret() {
    __asm__("pop rdx; ret");
}
void pop_rsi_ret() {
    __asm__("pop rsi; ret");
}
void pop_rax_ret() {
    __asm__("pop rax; ret");
}
void syscall_ret() {
    __asm__("syscall ; ret");
}

void telescope(size_t addr, int length) {
    for (int i = 0; i < length; i += 8) {
        printf("0x%lx\t| 0x%-20lx |", addr + i, *(size_t *)(addr + i));

        if (addr + i == tmp_bp - 8) {
            printf("\t<-- canary");
        } else if (addr + i == tmp_bp) {
            printf("\t<-- rbp");
        } else if (addr + i == tmp_bp + 8) {
            printf("\t<-- return address");
        } else if (addr + i == tmp_sp) {
            printf("\t<-- rsp");
        } else if (addr + i == tmp_rdi) {
            printf("\t<-- rdi");
        }
        puts("");
    }
}

void setup() {
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);
}

void hello() {
    printf(COLOR_MAGENTA
           "NEBULA nebudbg (NebuCTF 2023) NebuCTF-2023-12-03" COLOR_RESET "\n");
    printf("For help, type \"help\".\n");
}

void help_menu() {
    printf(COLOR_GREEN "help:" COLOR_RESET "\n");
    printf("\ttelescope [addr] [length=0x50] : show target addr, example: \n\t\ttelescope 0xdeadbeef 0x80\n");
    printf("\tstack [length=0x50] : show data on stack, example: \n\t\tstack 0x80\n");
    printf("\tset [addr] [data] : set value, example: \n\t\tset 0xdeadbeef 0xcafecafe\n");
    printf("\t" COLOR_RED "gift : gifts for u\n" COLOR_RESET);
    printf("\thelp : show this menu\n");
    printf("\tquit : leave nebudbg\n");
}

int main() {
    char buf[0xa0];
    char command[0x50];
    int argCount;
    long arg1, arg2;

    setup();
    hello();

    while (1) {

        printf(COLOR_RED "nebudbg> " COLOR_RESET);
        fgets(buf, 0xa0, stdin);

        argCount = sscanf(buf, "%s %lx %lx", command, &arg1, &arg2);

        if (!strcmp("help", command)) {
            help_menu();
        } else if (!strcmp("quit", command) || !strcmp("exit", command)) {
            break;
        } else if (!strncmp("telescope", command, 9) && argCount >= 2) {
            int length = 0x50;
            if (argCount > 2) {
                length = (int)arg2;
            }
            telescope(arg1, length);
        } else if (!strcmp("stack", command)) {
            int length = 0x50;
            if (argCount >= 2) {
                length = (int)arg1;
            }
            __asm__("mov tmp_bp, rbp;"
                    "mov tmp_sp, rsp;"
                    "mov tmp_rdi, rdi;");
            telescope((size_t)tmp_sp, length);
        } else if (!strcmp("gift", command)) {
            printf(COLOR_GREEN "Gifts:" COLOR_RESET "\n");
            printf("\t0x%-20lx -> pop rdi ; ret\n", (size_t)&pop_rdi_ret + 8);
            printf("\t0x%-20lx -> pop rsi ; ret\n", (size_t)&pop_rsi_ret + 8);
            printf("\t0x%-20lx -> pop rdx ; ret\n", (size_t)&pop_rdx_ret + 8);
            printf("\t0x%-20lx -> pop rax ; ret\n", (size_t)&pop_rax_ret + 8);
            printf("\t0x%-20lx -> syscall ; ret\n", (size_t)&syscall_ret + 8);
        } else if (!strcmp("set", command)) {
            if (argCount != 3) {
                help_menu();
                continue;
            }
            size_t target_addr = arg1;
            size_t target_value = arg2;
            *(long*)target_addr = target_value;
        }
    }

    return 0;
}

