package fr.hokanosekai;

import fr.hokanosekai.commands.FlagCommand;
import fr.hokanosekai.commands.WordusCommand;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.plugin.java.JavaPlugin;

public class Wordus extends JavaPlugin implements Listener {
    @Override
    public void onEnable() {
        getLogger().info("Wordus enabled");

        FlagCommand.register(this);
        WordusCommand.register(this);
        getServer().getPluginManager().registerEvents(this, this);
    }

    @Override
    public void onDisable() {
        getLogger().info("Wordus disabled");
    }

    @EventHandler
    public void onPlayerJoin(PlayerJoinEvent event) {
        event.getPlayer().sendMessage("Bienvenue sur mon serveur caché !");
        event.getPlayer().sendMessage("Tu peux faire la commande /flag pour récupérer le flag");
    }
}