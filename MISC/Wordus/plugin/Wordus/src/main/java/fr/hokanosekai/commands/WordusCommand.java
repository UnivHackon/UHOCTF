package fr.hokanosekai.commands;

import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.plugin.Plugin;
import org.jetbrains.annotations.NotNull;

public class WordusCommand extends Command {
    protected WordusCommand(@NotNull String name) {
         super(name);
    }

    public static void register(Plugin plugin) {
        plugin.getServer().getCommandMap().register("wordus", new WordusCommand("wordus"));
    }

    @Override
    public boolean execute(@NotNull CommandSender commandSender, @NotNull String s, @NotNull String[] strings) {
        if (commandSender instanceof Player player) {
            player.sendMessage("FLAG: UHOCTF{w0rdus_1s_4w3s0m3}");
        }
        return true;
    }
}
