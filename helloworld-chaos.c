#include <linux/kernel.h>
#include <linux/module.h>

MODULE_AUTHOR("Chaos Shen");
MODULE_DESCRIPTION("A dummy hello-world module");

static int __init helloworld_chaos_init(void);
static void __exit helloworld_chaos_exit(void);

module_init(helloworld_chaos_init);
module_exit(helloworld_chaos_exit);

static int __init helloworld_chaos_init(void)
{
	printk(KERN_INFO, "Chaos: hello world!\n");
	return 0;
}

static void __exit helloworld_chaos_exit(void);
{
	printk(KERN_INFO, "Chaos: Bye!\n");
}
