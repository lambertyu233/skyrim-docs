#pragma once

/*
* For modders: Copy this file into your own project if you wish to use this API
*/
namespace OAR_API::UI
{
	// Available UI interface versions
	enum class InterfaceVersion : uint8_t
	{
		V1,  // unsupported
		V2,
		V3,

		Latest = V3
	};

	// Open Animation Replacer's UI interface
	class IUIInterface2
	{
	public:
		/// <summary>
		/// Get Open Animation Replacer's ImGui context.
		/// </summary>
		/// <returns>A pointer to the ImGuiContext* object</returns>
		[[nodiscard]] virtual void* GetImGuiContext() noexcept = 0;

		/// <summary>
		/// Get Open Animation Replacer's ImGui allocator functions.
		/// </summary>
		/// <returns>Returns by reference - ImGuiMemAllocFunc*, ImGuiMemFreeFunc*, void**</returns>
		virtual void GetImGuiAllocatorFunctions(void* a_ptrAllocFunc, void* a_ptrFreeFunc, void** a_ptrUserData) noexcept = 0;

		/// <summary>
		///	Moves the ImGui cursor to the second column in Open Animation Replacer's UI layout.
		///	</summary>
		///	<param name="a_percent">The percentage of the window taken up by the first column</param>
		virtual void SecondColumn(float a_percent) noexcept = 0;

		/// <summary>
		///	Returns the width of the first column in Open Animation Replacer's UI layout.
		///	</summary>
		///	<param name="a_percent">The percentage of the window taken up by the first column</param>
		[[nodiscard]] virtual float GetFirstColumnWidth(float a_percent) noexcept = 0;
	};

	class IUIInterface3 : public IUIInterface2
	{
	public:
		/// <summary>
		/// Opens the Open Animation Replacer menu.
		/// </summary>
		/// <returns>Whether the operation was successful</returns>
		virtual bool OpenMenu() noexcept = 0;

		/// <summary>
		/// Closes the Open Animation Replacer menu.
		/// </summary>
		/// <returns>Whether the operation was successful</returns>
		virtual bool CloseMenu() noexcept = 0;

		/// <summary>
		/// Toggles the Open Animation Replacer menu.
		/// </summary>
		virtual void ToggleMenu() noexcept = 0;

		/// <summary>
		/// Checks if the Open Animation Replacer's menu is currently open.
		/// </summary>
		/// <returns>Whether the menu is currently open</returns>
		virtual bool IsMenuOpen() noexcept = 0;

		/// <summary>
		/// Suppresses the Open Animation Replacer's menu hotkey. Intended to be used by other plugins that manually open Open Animation Replacer's menu.
		/// </summary>
		/// <param name="a_bSuppress">Whether the hotkey should be suppressed or not</param>
		/// <param name="a_alternativeKeyData">The alternative key to be displayed in the UI banners instead of the set hotkey. Only used if a_bSuppress is true. The first member of the array is the key, and the following three indicate whether modifier keys Ctrl, Shift or Alt need to be held.</param>
		virtual void SetSuppressMenuHotkey(bool a_bSuppress, uint32_t a_alternativeKeyData[4] = {}) noexcept = 0;
	};

	using IUIInterface = IUIInterface3;

	using _RequestPluginAPI_UI = IUIInterface* (*)(InterfaceVersion a_interfaceVersion, const char* a_pluginName, REL::Version a_pluginVersion);

	/// <summary>
	/// Request the Open Animation Replacer UI API interface.
	/// </summary>
	/// <param name="a_interfaceVersion">The interface version to request</param>
	/// <returns>The pointer to the API singleton, or nullptr if request failed</returns>
	IUIInterface* GetAPI(InterfaceVersion a_interfaceVersion = InterfaceVersion::Latest);

	static inline bool bImGuiContextInitialized = false;

	/// <summary>
	/// Call this inside any of the functions that are supposed to use OpenAnimationReplacer's ImGui context, and call InitializeImGuiContext if this returns false.
	/// </summary>
	/// <returns>Whether the context is correctly set</returns>
	inline bool IsImGuiContextInitialized() { return bImGuiContextInitialized; }

	/// <summary>
	/// Call this to set up OpenAnimationReplacer's ImGui context as the current one.
	/// </summary>
	/// <returns>Whether the context is correctly set</returns>
	bool InitializeImGuiContext();
}

extern OAR_API::UI::IUIInterface* g_oarUIInterface;
