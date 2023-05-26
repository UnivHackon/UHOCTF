package fr.hokanosekai.commands;

import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.plugin.Plugin;
import org.jetbrains.annotations.NotNull;

public class FlagCommand extends @NotNull Command {

    protected FlagCommand(@NotNull String name) {
        super(name);
    }

    public static void register(Plugin plugin) {
        plugin.getServer().getCommandMap().register("flag", new FlagCommand("flag"));
    }

    @Override
    public boolean execute(@NotNull CommandSender commandSender, @NotNull String s, @NotNull String[] strings) {
        if (commandSender instanceof Player player) {
            // Kick the player
            player.kickPlayer("HEHE je t'ai kické");
        }
        return true;
    }
}
